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
            panelTopbar = new Panel();
            label2 = new Label();
            tbSearch = new TextBox();
            lblTitle = new Label();
            btnNewRoom = new Button();
            lblEmpty = new Label();
            dataGridViewRooms = new DataGridView();
            panel3 = new Panel();
            panelTopbar.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridViewRooms).BeginInit();
            panel3.SuspendLayout();
            SuspendLayout();
            // 
            // panelTopbar
            // 
            panelTopbar.BackColor = Color.MediumPurple;
            panelTopbar.Controls.Add(label2);
            panelTopbar.Controls.Add(tbSearch);
            panelTopbar.Controls.Add(lblTitle);
            panelTopbar.Controls.Add(btnNewRoom);
            panelTopbar.Dock = DockStyle.Top;
            panelTopbar.Location = new Point(0, 0);
            panelTopbar.Margin = new Padding(5, 4, 5, 4);
            panelTopbar.Name = "panelTopbar";
            panelTopbar.Size = new Size(875, 79);
            panelTopbar.TabIndex = 1;
            panelTopbar.MouseDown += panelTopbar_MouseDown;
            panelTopbar.MouseMove += panelTopbar_MouseMove;
            panelTopbar.MouseUp += panelTopbar_MouseUp;
            // 
            // label2
            // 
            label2.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            label2.AutoSize = true;
            label2.Font = new Font("Courier New", 10F);
            label2.ForeColor = Color.Lavender;
            label2.Location = new Point(490, 9);
            label2.Name = "label2";
            label2.Size = new Size(129, 20);
            label2.TabIndex = 7;
            label2.Text = "SEARCH NAME:";
            // 
            // tbSearch
            // 
            tbSearch.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            tbSearch.BackColor = Color.Lavender;
            tbSearch.Location = new Point(490, 32);
            tbSearch.Name = "tbSearch";
            tbSearch.PlaceholderText = "A14";
            tbSearch.Size = new Size(225, 34);
            tbSearch.TabIndex = 6;
            tbSearch.TextChanged += tbSearch_TextChanged;
            // 
            // lblTitle
            // 
            lblTitle.AutoSize = true;
            lblTitle.Font = new Font("Courier New", 16F);
            lblTitle.ForeColor = Color.Lavender;
            lblTitle.Location = new Point(59, 24);
            lblTitle.Margin = new Padding(5, 0, 5, 0);
            lblTitle.Name = "lblTitle";
            lblTitle.Size = new Size(93, 30);
            lblTitle.TabIndex = 0;
            lblTitle.Text = "ROOMS";
            // 
            // btnNewRoom
            // 
            btnNewRoom.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnNewRoom.BackColor = Color.Lavender;
            btnNewRoom.FlatAppearance.BorderSize = 0;
            btnNewRoom.FlatStyle = FlatStyle.Flat;
            btnNewRoom.Location = new Point(729, 24);
            btnNewRoom.Name = "btnNewRoom";
            btnNewRoom.Size = new Size(121, 43);
            btnNewRoom.TabIndex = 5;
            btnNewRoom.Text = "NEW";
            btnNewRoom.UseVisualStyleBackColor = false;
            btnNewRoom.Click += btnNewRoom_Click;
            // 
            // lblEmpty
            // 
            lblEmpty.AutoSize = true;
            lblEmpty.BackColor = Color.Lavender;
            lblEmpty.Font = new Font("Courier New", 16F);
            lblEmpty.ForeColor = Color.MediumPurple;
            lblEmpty.Location = new Point(324, 171);
            lblEmpty.Margin = new Padding(5, 0, 5, 0);
            lblEmpty.Name = "lblEmpty";
            lblEmpty.Size = new Size(221, 30);
            lblEmpty.TabIndex = 3;
            lblEmpty.Text = "NO ROOMS YET.";
            // 
            // dataGridViewRooms
            // 
            dataGridViewRooms.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            dataGridViewRooms.BackgroundColor = Color.Lavender;
            dataGridViewRooms.BorderStyle = BorderStyle.None;
            dataGridViewRooms.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            dataGridViewRooms.Location = new Point(19, 20);
            dataGridViewRooms.Margin = new Padding(10);
            dataGridViewRooms.Name = "dataGridViewRooms";
            dataGridViewRooms.RowHeadersWidth = 51;
            dataGridViewRooms.Size = new Size(844, 402);
            dataGridViewRooms.TabIndex = 2;
            // 
            // panel3
            // 
            panel3.BackColor = Color.Lavender;
            panel3.Controls.Add(lblEmpty);
            panel3.Controls.Add(dataGridViewRooms);
            panel3.Dock = DockStyle.Fill;
            panel3.Location = new Point(0, 79);
            panel3.Margin = new Padding(10);
            panel3.Name = "panel3";
            panel3.Padding = new Padding(10);
            panel3.Size = new Size(875, 441);
            panel3.TabIndex = 6;
            // 
            // RoomForm
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(875, 520);
            Controls.Add(panel3);
            Controls.Add(panelTopbar);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "RoomForm";
            StartPosition = FormStartPosition.Manual;
            Text = "RoomForm";
            FormClosed += RoomForm_FormClosed;
            panelTopbar.ResumeLayout(false);
            panelTopbar.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)dataGridViewRooms).EndInit();
            panel3.ResumeLayout(false);
            panel3.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Panel panelTopbar;
        private Label lblTitle;
        private Label lblEmpty;
        private DataGridView dataGridViewRooms;
        private Button btnNewRoom;
        private Label label2;
        private TextBox tbSearch;
        private Panel panel3;
    }
}