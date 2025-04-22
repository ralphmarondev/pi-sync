namespace PiSync.Room
{
    partial class RoomForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            panel1 = new Panel();
            label3 = new Label();
            dataGridViewRooms = new DataGridView();
            lblEmpty = new Label();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridViewRooms).BeginInit();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.MediumPurple;
            panel1.Controls.Add(label3);
            panel1.Dock = DockStyle.Top;
            panel1.Location = new Point(0, 0);
            panel1.Margin = new Padding(5, 4, 5, 4);
            panel1.Name = "panel1";
            panel1.Size = new Size(875, 79);
            panel1.TabIndex = 1;
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Courier New", 16F);
            label3.ForeColor = Color.Lavender;
            label3.Location = new Point(59, 24);
            label3.Margin = new Padding(5, 0, 5, 0);
            label3.Name = "label3";
            label3.Size = new Size(93, 30);
            label3.TabIndex = 0;
            label3.Text = "ROOMS";
            // 
            // dataGridViewRooms
            // 
            dataGridViewRooms.BackgroundColor = Color.GhostWhite;
            dataGridViewRooms.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewRooms.Dock = DockStyle.Fill;
            dataGridViewRooms.Location = new Point(0, 79);
            dataGridViewRooms.Margin = new Padding(10);
            dataGridViewRooms.Name = "dataGridViewRooms";
            dataGridViewRooms.RowHeadersWidth = 51;
            dataGridViewRooms.Size = new Size(875, 441);
            dataGridViewRooms.TabIndex = 2;
            // 
            // lblEmpty
            // 
            lblEmpty.AutoSize = true;
            lblEmpty.BackColor = Color.GhostWhite;
            lblEmpty.Font = new Font("Courier New", 16F);
            lblEmpty.ForeColor = Color.MediumPurple;
            lblEmpty.Location = new Point(344, 258);
            lblEmpty.Margin = new Padding(5, 0, 5, 0);
            lblEmpty.Name = "lblEmpty";
            lblEmpty.Size = new Size(221, 30);
            lblEmpty.TabIndex = 3;
            lblEmpty.Text = "NO ROOMS YET.";
            // 
            // RoomForm
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(875, 520);
            Controls.Add(lblEmpty);
            Controls.Add(dataGridViewRooms);
            Controls.Add(panel1);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "RoomForm";
            StartPosition = FormStartPosition.Manual;
            Text = "RoomForm";
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridViewRooms).EndInit();
            ResumeLayout(false);
            PerformLayout();
        }

        #endregion

        private Panel panel1;
        private Label label3;
        private DataGridView dataGridViewRooms;
        private Label lblEmpty;
    }
}