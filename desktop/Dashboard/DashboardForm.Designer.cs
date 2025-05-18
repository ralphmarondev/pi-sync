namespace PiSync.Dashboard
{
    partial class DashboardForm
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(DashboardForm));
            panel1 = new Panel();
            btnFullScreen = new PictureBox();
            btnAdminName = new Label();
            pictureBox1 = new PictureBox();
            lblTitle = new Label();
            panelRooms = new FlowLayoutPanel();
            panel1.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)btnFullScreen).BeginInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).BeginInit();
            SuspendLayout();
            // 
            // panel1
            // 
            panel1.BackColor = Color.MediumPurple;
            panel1.Controls.Add(btnFullScreen);
            panel1.Controls.Add(btnAdminName);
            panel1.Controls.Add(pictureBox1);
            panel1.Controls.Add(lblTitle);
            panel1.Dock = DockStyle.Top;
            panel1.Location = new Point(0, 0);
            panel1.Name = "panel1";
            panel1.Size = new Size(875, 79);
            panel1.TabIndex = 0;
            panel1.MouseDown += panel1_MouseDown;
            panel1.MouseMove += panel1_MouseMove;
            panel1.MouseUp += panel1_MouseUp;
            // 
            // btnFullScreen
            // 
            btnFullScreen.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnFullScreen.BackColor = Color.White;
            btnFullScreen.Cursor = Cursors.Hand;
            btnFullScreen.Image = (Image)resources.GetObject("btnFullScreen.Image");
            btnFullScreen.Location = new Point(823, 28);
            btnFullScreen.Name = "btnFullScreen";
            btnFullScreen.Size = new Size(40, 40);
            btnFullScreen.SizeMode = PictureBoxSizeMode.Zoom;
            btnFullScreen.TabIndex = 4;
            btnFullScreen.TabStop = false;
            btnFullScreen.Click += btnFullScreen_Click;
            // 
            // btnAdminName
            // 
            btnAdminName.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            btnAdminName.AutoSize = true;
            btnAdminName.Cursor = Cursors.Hand;
            btnAdminName.ForeColor = Color.White;
            btnAdminName.Location = new Point(468, 33);
            btnAdminName.Name = "btnAdminName";
            btnAdminName.Size = new Size(194, 25);
            btnAdminName.TabIndex = 3;
            btnAdminName.Text = "ADMINISTRATOR";
            btnAdminName.Click += btnAdminName_Click;
            btnAdminName.MouseDown += btnAdminName_MouseDown;
            btnAdminName.MouseMove += btnAdminName_MouseMove;
            btnAdminName.MouseUp += btnAdminName_MouseUp;
            // 
            // pictureBox1
            // 
            pictureBox1.Anchor = AnchorStyles.Top | AnchorStyles.Right;
            pictureBox1.BackColor = Color.White;
            pictureBox1.Image = Properties.Resources.icons8_test_account_80;
            pictureBox1.Location = new Point(422, 28);
            pictureBox1.Name = "pictureBox1";
            pictureBox1.Size = new Size(40, 40);
            pictureBox1.SizeMode = PictureBoxSizeMode.Zoom;
            pictureBox1.TabIndex = 2;
            pictureBox1.TabStop = false;
            pictureBox1.MouseDown += pictureBox1_MouseDown;
            pictureBox1.MouseMove += pictureBox1_MouseMove;
            pictureBox1.MouseUp += pictureBox1_MouseUp;
            // 
            // lblTitle
            // 
            lblTitle.AutoSize = true;
            lblTitle.Font = new Font("Courier New", 16F);
            lblTitle.ForeColor = Color.Lavender;
            lblTitle.Location = new Point(46, 28);
            lblTitle.Margin = new Padding(5, 0, 5, 0);
            lblTitle.Name = "lblTitle";
            lblTitle.Size = new Size(157, 30);
            lblTitle.TabIndex = 1;
            lblTitle.Text = "DASHBOARD";
            lblTitle.MouseDown += lblTitle_MouseDown;
            lblTitle.MouseMove += lblTitle_MouseMove;
            lblTitle.MouseUp += lblTitle_MouseUp;
            // 
            // panelRooms
            // 
            panelRooms.AutoScroll = true;
            panelRooms.Dock = DockStyle.Fill;
            panelRooms.Location = new Point(0, 79);
            panelRooms.Name = "panelRooms";
            panelRooms.Size = new Size(875, 441);
            panelRooms.TabIndex = 1;
            // 
            // DashboardForm
            // 
            AutoScaleDimensions = new SizeF(14F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(875, 520);
            Controls.Add(panelRooms);
            Controls.Add(panel1);
            Font = new Font("Courier New", 13.8F, FontStyle.Regular, GraphicsUnit.Point, 0);
            FormBorderStyle = FormBorderStyle.None;
            Margin = new Padding(5, 4, 5, 4);
            Name = "DashboardForm";
            Text = "DashboardForm";
            FormClosed += DashboardForm_FormClosed;
            Load += DashboardForm_Load;
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)btnFullScreen).EndInit();
            ((System.ComponentModel.ISupportInitialize)pictureBox1).EndInit();
            ResumeLayout(false);
        }

        #endregion
        private Label lblTitle;
        private Panel panel1;
        private FlowLayoutPanel panelRooms;
        private PictureBox btnFullScreen;
        private Label btnAdminName;
        private PictureBox pictureBox1;
    }
}